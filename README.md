# voltaTrees 🌴🌴

A LLVM-based compiler for XGBoost and LightGBM decision trees.

`voltatrees` converts trained XGBoost and LightGBM models to optimized machine code, speeding-up prediction by ≥10x.

## Example

```python
import voltatrees as vt

model = vt.XGBoostRegressor.Model(model_file="NYC_taxi/model.txt")
model.compile()
model.predict(df)
```

## Installation

```bash
git clone git clone https://github.com/VoltaML/volta-trees.git
cd volta-trees/
pip install -e .
```

## Benchmarks

(TBD on bare-metal machine)

