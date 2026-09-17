#!/usr/bin/env python3
import json, subprocess

def _run(cmd, timeout=240):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)

def invoke(space, prompt):
    info=_run(['hf-gradio','info',space],120)
    if info.returncode!=0:
        return False,'',{'stage':'info','error':(info.stderr or info.stdout)[-1000:]}
    try: api=json.loads(info.stdout)
    except Exception as e: return False,'',{'stage':'decode','error':repr(e)}
    pref=['/generate','/chat','/predict','/respond','/infer','/run']
    eps=list(api.items()); eps.sort(key=lambda kv:(pref.index(kv[0]) if kv[0] in pref else 99,kv[0]))
    for endpoint,spec in eps:
        payload={}; prompt_set=False; bad=False
        for p in spec.get('parameters',[]):
            n=p.get('name',''); l=n.lower(); req=bool(p.get('required',False)); default=p.get('default'); typ=(p.get('type') or {}).get('type')
            if l in {'message','prompt','text','query','input','instruction','user_message'}: payload[n]=prompt; prompt_set=True
            elif l in {'chat_history','history','messages'}: payload[n]=[]
            elif l in {'max_new_tokens','max_tokens','maximum_new_tokens'}: payload[n]=800
            elif l=='temperature': payload[n]=0.1
            elif l=='top_p': payload[n]=0.9
            elif l in {'system','system_prompt'}: payload[n]='Rigorous Collatz dynamics researcher. CLAIM<=EVIDENCE.'
            elif req and default is None:
                if typ=='string' and not prompt_set: payload[n]=prompt; prompt_set=True
                else: bad=True; break
        if bad or not prompt_set: continue
        r=_run(['hf-gradio','predict',space,endpoint,json.dumps(payload,ensure_ascii=False)],240)
        if r.returncode==0 and (r.stdout or '').strip():
            raw=r.stdout.strip()
            try:
                obj=json.loads(raw)
                if isinstance(obj,dict):
                    for k in ('Response','response','text','output','message'):
                        if isinstance(obj.get(k),str): return True,obj[k].strip(),{'endpoint':endpoint}
            except: pass
            return True,raw,{'endpoint':endpoint}
    return False,'',{'stage':'predict','error':'No compatible successful endpoint'}
