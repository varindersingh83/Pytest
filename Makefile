nodes?=4

prepare:
	docker-compose up -d && docker-compose scale chrome=$(nodes)

test:
	docker-compose exec tester pytest -s -v -n=4 testcases/test1.py

test_maybe:
	docker run test/runner pytest -s -v -n=4 testcases/test1.py

status:
	docker-compose ps

clean:
	docker-compose down
