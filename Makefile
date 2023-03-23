PKG_NAME := ripgrep
URL = https://github.com/BurntSushi/ripgrep/archive/refs/tags/13.0.0.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/vendor/ripgrep/snapshot/ripgrep-2023-03-23-21-22-40.tar.xz ./vendor

include ../common/Makefile.common
