import json,hashlib,pathlib,platform
items=[("structure",420.,.20),("propulsion",310.,.15),("avionics",95.,.25),("thermal",80.,.20)]
cbe=sum(m for _,m,_ in items);alloc=sum(m*(1+margin) for _,m,margin in items);ok=alloc>cbe
out={"cbe_mass_kg":cbe,"mass_with_margins_kg":alloc,"aggregate_margin_kg":alloc-cbe,"aggregate_margin_fraction":alloc/cbe-1,"farm":143,"engine":"python-engineering-batch-canary","engine_version":platform.python_version(),"test":"MASS_MARGIN_ROLLUP","status":"REAL_ENGINE_CANARY_OK" if ok else "FAIL","epistemic_status":"ENGINEERING_CANARY_NOT_PHYSICAL_VALIDATION"}
raw=json.dumps(out,sort_keys=True).encode();out["result_sha256"]=hashlib.sha256(raw).hexdigest();pathlib.Path("artifacts").mkdir(exist_ok=True);pathlib.Path("artifacts/f143_engine_canary.json").write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out));raise SystemExit(0 if ok else 1)
