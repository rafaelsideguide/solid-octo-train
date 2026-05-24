.PHONY: eval eval-fresh

eval:
	python -m eval.run_eval

eval-fresh:
	python -m eval.run_eval --fresh-judge
