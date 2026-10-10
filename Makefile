up:
	docker compose up --build -d
down:
	docker compose down
logs:
	docker compose logs -f
validate:
	python scripts/validate_yaml.py
k8s-apply:
	kubectl apply -f k8s/namespace.yaml
	kubectl apply -f k8s/deployment.yaml -f k8s/service.yaml
