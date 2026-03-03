# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: a_maze_ing                                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026                                    #+#    #+#              #
#    Updated: 2026                                   ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

PYTHON		= python3
MAIN		= a_maze_ing.py
CONFIG		= config.txt
WHL			= $(wildcard mazegen-*.whl)

# ── Couleurs terminal ────────────────────────────────────────────────────────
GREEN		= \033[0;32m
YELLOW		= \033[0;33m
CYAN		= \033[0;36m
RED			= \033[0;31m
RESET		= \033[0m
BOLD		= \033[1m

.DEFAULT_GOAL := help

install:
	@echo "$(YELLOW)>>> Installation des dépendances...$(RESET)"
	pip install -r requirements.txt --break-system-packages
	@if [ -n "$(WHL)" ]; then \
		echo "$(YELLOW)>>> Installation du module mazegen : $(WHL)$(RESET)"; \
		pip install $(WHL) --break-system-packages; \
	else \
		echo "$(RED)>>> Aucun fichier mazegen-*.whl trouvé, skipping...$(RESET)"; \
	fi
	@echo "$(GREEN)>>> Installation terminée.$(RESET)"

run:
	@echo "$(CYAN)>>> Lancement de A-Maze-ing...$(RESET)"
	$(PYTHON) $(MAIN) $(CONFIG)

debug:
	@echo "$(YELLOW)>>> Mode debug (pdb)...$(RESET)"
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)

lint:
	@echo "$(YELLOW)>>> flake8...$(RESET)"
	flake8 .
	@echo "$(YELLOW)>>> mypy...$(RESET)"
	mypy . --warn-return-any \
	       --warn-unused-ignores \
	       --ignore-missing-imports \
	       --disallow-untyped-defs \
	       --check-untyped-defs
	@echo "$(GREEN)>>> Lint OK.$(RESET)"

clean:
	@echo "$(YELLOW)>>> Nettoyage...$(RESET)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	find . -name "*.pyo" -delete 2>/dev/null || true
	@echo "$(GREEN)>>> Nettoyage terminé.$(RESET)"

.PHONY: install run debug lint clean