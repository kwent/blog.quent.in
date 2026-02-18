.PHONY: help install dev serve build lint format check new-post covers check-links clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install tools and dependencies
	mise install
	uv sync

dev: ## Install with dev dependencies (linter)
	mise install
	uv sync --group dev

serve: ## Start Hugo dev server
	hugo server -D

build: ## Build static site
	hugo

lint: ## Run linter
	uv run --group dev ruff check scripts/
	uv run --group dev ruff format --check scripts/

format: ## Auto-format and fix lint issues
	uv run --group dev ruff check --fix scripts/
	uv run --group dev ruff format scripts/

check: lint ## Run all checks (alias for lint)

new-post: ## Create new post (usage: make new-post TITLE="My Title" TAGS="tag1,tag2")
	uv run scripts/new_post.py "$(TITLE)" $(if $(TAGS),--tags $(TAGS)) $(if $(CATS),--categories $(CATS))

covers: ## Backfill missing cover images
	uv run scripts/generate_covers.py

check-links: ## Check for broken links
	uv run scripts/check_links.py

clean: ## Clean build artifacts
	rm -rf public/ resources/_gen/
