## Generate setup.py by poetry command for shared package

PACKAGE = ls_pyenv

.PHONY: build-package, install, install-pipx, clean
build-package:
	$(eval VERSION := $(shell poetry version -s))
	poetry build
	@tar zxf dist/$(PACKAGE)-$(VERSION).tar.gz -C ./dist
	@cp dist/$(PACKAGE)-$(VERSION)/setup.py setup.py
	@rm -rf dist

install: build-package
	python setup.py install

install-pipx: build-package
	pipx install .

uninstall:
	pip uninstall -y $(PACKAGE)

uninstall-pipx:
	pipx uninstall $(PACKAGE)

clean:
	@rm -rf dist
	@rm -rf build
	@rm -rf $(PACKAGE).egg-info
	@rm -f setup.py
