run:
	astmutate/mutator.py example/nayajson.py example/nayajson_test.py 

debug:
	python3 -mpudb astmutate/mutator.py example/nayajson.py example/nayajson_test.py 


clean:
	rm -rf __pycache__
