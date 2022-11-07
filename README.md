# VoltaTrees 

A LLVM-based compiler for XGBoost and LightGBM decision trees.

`voltatrees` converts trained XGBoost and LightGBM models to optimized machine code, speeding-up prediction by ≥10x.

## Example

```python
import voltatrees.volta_XGBM as vxgb

model = vxgb.Model(model_file="NYC_taxi/xgb_model.txt")
model.compile()
model.predict(df)
```

```python
import voltatrees.volta_LGBM as vlgb

model = vlgb.Model(model_file="NYC_taxi/lgb_model.txt")
model.compile()
model.predict(df)
```


## Installation
```bash
git clone https://github.com/VoltaML/volta-trees.git
cd volta-trees/
pip install -e .
```

## Benchmarks

(TBD on bare-metal machine)

## Development 

```bash
git clone git clone https://github.com/VoltaML/volta-trees.git
cd volta-trees/
pip install -e .
```
