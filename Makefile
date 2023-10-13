run-app:
	cd me && uvicorn main:app --reload

test:
	pytest
