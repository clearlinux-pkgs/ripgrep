PKG_NAME := ripgrep
URL = https://github.com/BurntSushi/ripgrep/archive/14.1.1/ripgrep-14.1.1.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/vendor/ripgrep/snapshot/ripgrep-2024-01-09-22-23-02.tar.gz ./vendor $(CGIT_BASE_URL)/vendor/ripgrep/snapshot/ripgrep-2024-09-09-15-45-32.tar.xz ./vendor

include ../common/Makefile.common
