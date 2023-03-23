#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cargo
#
Name     : ripgrep
Version  : 13.0.0
Release  : 3
URL      : https://github.com/BurntSushi/ripgrep/archive/refs/tags/13.0.0.tar.gz
Source0  : https://github.com/BurntSushi/ripgrep/archive/refs/tags/13.0.0.tar.gz
Source1  : http://localhost/cgit/vendor/ripgrep/snapshot/ripgrep-2023-03-23-21-22-40.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause BSL-1.0 ICU MIT Unicode-DFS-2016 Unlicense
Requires: ripgrep-bin = %{version}-%{release}
Requires: ripgrep-license = %{version}-%{release}
BuildRequires : rustc
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains updated benchmarks as of 2018-01-08. They were captured
via the benchsuite script at `benchsuite/benchsuite` from the root of this
repository. The command that was run:

%package bin
Summary: bin components for the ripgrep package.
Group: Binaries
Requires: ripgrep-license = %{version}-%{release}

%description bin
bin components for the ripgrep package.


%package license
Summary: license components for the ripgrep package.
Group: Default

%description license
license components for the ripgrep package.


%prep
%setup -q -n ripgrep-13.0.0
cd %{_builddir}
tar xf %{_sourcedir}/ripgrep-2023-03-23-21-22-40.tar.xz
cd %{_builddir}/ripgrep-13.0.0
mkdir -p ./vendor
cp -r %{_builddir}/ripgrep-2023-03-23-21-22-40/* %{_builddir}/ripgrep-13.0.0/./vendor

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
mkdir -p .cargo
echo '[source.crates-io]' >> .cargo/config.toml
echo 'replace-with = "vendored-sources"' >> .cargo/config.toml
echo '[source.vendored-sources]' >> .cargo/config.toml
echo 'directory = "vendor"' >> .cargo/config.toml
cargo build --release

%install
mkdir -p %{buildroot}/usr/share/package-licenses/ripgrep
cp %{_builddir}/ripgrep-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/ripgrep-%{version}/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-%{version}/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-%{version}/crates/cli/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-%{version}/crates/cli/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-%{version}/crates/globset/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/ripgrep-%{version}/crates/globset/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-%{version}/crates/globset/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-%{version}/crates/grep/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/ripgrep-%{version}/crates/grep/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-%{version}/crates/grep/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-%{version}/crates/ignore/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/ripgrep-%{version}/crates/ignore/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-%{version}/crates/ignore/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-%{version}/crates/matcher/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-%{version}/crates/matcher/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-%{version}/crates/pcre2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-%{version}/crates/pcre2/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-%{version}/crates/printer/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-%{version}/crates/printer/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-%{version}/crates/regex/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-%{version}/crates/regex/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-%{version}/crates/searcher/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-%{version}/crates/searcher/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/aho-corasick/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/aho-corasick/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/aho-corasick/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/atty/LICENSE %{buildroot}/usr/share/package-licenses/ripgrep/3acad00f27f89710cd66d3f5528aed5046ac28d9 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/base64/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/base64/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/bitflags/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/bitflags/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/bstr/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/93e25f7a8d77fb5a09acece508d3651054a1b123 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/bstr/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/bstr/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/99b5dc64e06bf0354ef3baac0ea25c929e4e3a9a || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/bstr/src/unicode/data/LICENSE-UNICODE %{buildroot}/usr/share/package-licenses/ripgrep/c4f8de16c29dc84a94d610b716fb1c9c7f143582 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/bytecount/LICENSE.Apache2 %{buildroot}/usr/share/package-licenses/ripgrep/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/bytecount/LICENSE.MIT %{buildroot}/usr/share/package-licenses/ripgrep/9ec2af04328d0eb6ec89ca6d75156ffc7aecf869 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/cc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/cc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/cfg-if-0.1.10/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/cfg-if-0.1.10/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/cfg-if/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/cfg-if/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/clap/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/2111f90a2fa5afba10ae753c5ca31a1d8080f597 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/crossbeam-channel/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/crossbeam-channel/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/144111aa0f14ef5a181326683aa9ebbd9252bca6 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/crossbeam-utils/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/crossbeam-utils/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/144111aa0f14ef5a181326683aa9ebbd9252bca6 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/encoding_rs/COPYRIGHT %{buildroot}/usr/share/package-licenses/ripgrep/5e356a6c9455af53dd119e65b6a82958cbc05c55 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/encoding_rs/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/encoding_rs/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/b4872d72eb3ccfa74730cc229184eec04f303e7d || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/encoding_rs_io/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/93e25f7a8d77fb5a09acece508d3651054a1b123 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/encoding_rs_io/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/encoding_rs_io/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/fnv/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/fnv/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/50121d8b8c9f6483fe17ea679f28f85fe59b2a5a || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/fs_extra/LICENSE %{buildroot}/usr/share/package-licenses/ripgrep/f2515ca1c978fa1b1d6e13a8a9ae63a36a2d52cd || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/glob/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/glob/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/hermit-abi/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/hermit-abi/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/itoa/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/itoa/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/jemalloc-sys/jemalloc/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/32366cf8c310f3ab4c264217764166f95f030e00 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/jemalloc-sys/rep/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/c797cef3f1b13a960a5119a084fb88529a924fd7 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/jemallocator/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/jemallocator/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/jobserver/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/jobserver/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/lazy_static/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/lazy_static/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/2bf5cac862d5a0480b5d5bcd3a1852d68bfeee84 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/libc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/libc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/36d69bcb88153a640740000efe933b009420ce7e || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/libm/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/libm/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/744183c4ca46703f4b738aca20e238e11c9a3b12 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/log/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/aca374a3362a76702c50bd4e7d590a57f8834fc7 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/log/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/f9cc84dfc567fdc0979fddc3e6257191d8ebc9d8 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/memchr/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/memchr/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/memchr/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/memmap2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/c1f96d6a54446beefad79ef49b3c123c597b7a40 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/memmap2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/e22df6a40db2eb4307dbc53b2cffa548e2bcbd2c || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/num_cpus/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/num_cpus/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/ec9737a4e769cce48d5c95d9c75a4ba5f29a2563 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/once_cell/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/once_cell/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/packed_simd_2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/aca374a3362a76702c50bd4e7d590a57f8834fc7 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/packed_simd_2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/f9cc84dfc567fdc0979fddc3e6257191d8ebc9d8 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/pcre2-sys/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/pcre2-sys/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/2ad1215c12bd0a3492399dc438aa63084323c662 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/pcre2-sys/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/pcre2-sys/pcre2/LICENCE %{buildroot}/usr/share/package-licenses/ripgrep/7bfc859266eab20c52c817c627c0782c20263c8e || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/pcre2-sys/pcre2/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/ripgrep/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/pcre2/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/pcre2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/2ad1215c12bd0a3492399dc438aa63084323c662 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/pcre2/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/pkg-config/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/pkg-config/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/proc-macro2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/proc-macro2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/quote/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/quote/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/regex-automata/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/regex-automata/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/regex-automata/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/regex-automata/data/fowler-tests/LICENSE %{buildroot}/usr/share/package-licenses/ripgrep/553e82bef8637312393c95bc62e23e8f81fd9e47 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/regex-automata/data/tests/fowler/LICENSE %{buildroot}/usr/share/package-licenses/ripgrep/553e82bef8637312393c95bc62e23e8f81fd9e47 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/regex-syntax/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/regex-syntax/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/regex-syntax/src/unicode_tables/LICENSE-UNICODE %{buildroot}/usr/share/package-licenses/ripgrep/68d12a03b339648117165b9c021b93f26974d6f6 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/regex/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/regex/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/regex/src/testdata/LICENSE %{buildroot}/usr/share/package-licenses/ripgrep/553e82bef8637312393c95bc62e23e8f81fd9e47 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/ryu/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/ryu/LICENSE-BOOST %{buildroot}/usr/share/package-licenses/ripgrep/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/same-file/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/same-file/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/2ad1215c12bd0a3492399dc438aa63084323c662 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/same-file/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/serde/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/serde/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/serde_derive/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/serde_derive/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/serde_json/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/serde_json/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/strsim/LICENSE %{buildroot}/usr/share/package-licenses/ripgrep/14be3fb1db517b371b463625246427013600f126 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/syn/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/syn/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/termcolor/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/termcolor/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/termcolor/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/textwrap/LICENSE %{buildroot}/usr/share/package-licenses/ripgrep/70e36c2f54755e87728778c41ab4b809e5b0b502 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/thread_local/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/thread_local/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/unicode-width/COPYRIGHT %{buildroot}/usr/share/package-licenses/ripgrep/5ed53061419caf64f84d064f3641392a2a10fa7f || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/unicode-width/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/unicode-width/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/60c3522081bf15d7ac1d4c5a63de425ef253e87a || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/unicode-xid/COPYRIGHT %{buildroot}/usr/share/package-licenses/ripgrep/5ed53061419caf64f84d064f3641392a2a10fa7f || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/unicode-xid/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/unicode-xid/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/60c3522081bf15d7ac1d4c5a63de425ef253e87a || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/walkdir/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/walkdir/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/walkdir/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/winapi-util/COPYING %{buildroot}/usr/share/package-licenses/ripgrep/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/winapi-util/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/2ad1215c12bd0a3492399dc438aa63084323c662 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/winapi-util/UNLICENSE %{buildroot}/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/winapi/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/ripgrep/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/ripgrep-2023-03-23-21-22-40/winapi/LICENSE-MIT %{buildroot}/usr/share/package-licenses/ripgrep/2243f7a86daaa727d34d92e987a741036f288464 || :
cargo install --path .
mkdir -p %{buildroot}/usr/bin
pushd "${HOME}/.cargo/bin/"
mv * %{buildroot}/usr/bin/
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ripgrep/144111aa0f14ef5a181326683aa9ebbd9252bca6
/usr/share/package-licenses/ripgrep/14be3fb1db517b371b463625246427013600f126
/usr/share/package-licenses/ripgrep/2111f90a2fa5afba10ae753c5ca31a1d8080f597
/usr/share/package-licenses/ripgrep/2243f7a86daaa727d34d92e987a741036f288464
/usr/share/package-licenses/ripgrep/2ad1215c12bd0a3492399dc438aa63084323c662
/usr/share/package-licenses/ripgrep/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/ripgrep/2bf5cac862d5a0480b5d5bcd3a1852d68bfeee84
/usr/share/package-licenses/ripgrep/32366cf8c310f3ab4c264217764166f95f030e00
/usr/share/package-licenses/ripgrep/36d69bcb88153a640740000efe933b009420ce7e
/usr/share/package-licenses/ripgrep/3acad00f27f89710cd66d3f5528aed5046ac28d9
/usr/share/package-licenses/ripgrep/3b042d3d971924ec0296687efd50dbe08b734976
/usr/share/package-licenses/ripgrep/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/ripgrep/4c8990add9180fc59efa5b0d8faf643c9709501e
/usr/share/package-licenses/ripgrep/50121d8b8c9f6483fe17ea679f28f85fe59b2a5a
/usr/share/package-licenses/ripgrep/553e82bef8637312393c95bc62e23e8f81fd9e47
/usr/share/package-licenses/ripgrep/5798832c31663cedc1618d18544d445da0295229
/usr/share/package-licenses/ripgrep/5e356a6c9455af53dd119e65b6a82958cbc05c55
/usr/share/package-licenses/ripgrep/5ed53061419caf64f84d064f3641392a2a10fa7f
/usr/share/package-licenses/ripgrep/60c3522081bf15d7ac1d4c5a63de425ef253e87a
/usr/share/package-licenses/ripgrep/68d12a03b339648117165b9c021b93f26974d6f6
/usr/share/package-licenses/ripgrep/70e36c2f54755e87728778c41ab4b809e5b0b502
/usr/share/package-licenses/ripgrep/744183c4ca46703f4b738aca20e238e11c9a3b12
/usr/share/package-licenses/ripgrep/7bfc859266eab20c52c817c627c0782c20263c8e
/usr/share/package-licenses/ripgrep/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/ripgrep/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/ripgrep/93e25f7a8d77fb5a09acece508d3651054a1b123
/usr/share/package-licenses/ripgrep/99b5dc64e06bf0354ef3baac0ea25c929e4e3a9a
/usr/share/package-licenses/ripgrep/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
/usr/share/package-licenses/ripgrep/9ec2af04328d0eb6ec89ca6d75156ffc7aecf869
/usr/share/package-licenses/ripgrep/9f3c36d2b7d381d9cf382a00166f3fbd06783636
/usr/share/package-licenses/ripgrep/aca374a3362a76702c50bd4e7d590a57f8834fc7
/usr/share/package-licenses/ripgrep/b4872d72eb3ccfa74730cc229184eec04f303e7d
/usr/share/package-licenses/ripgrep/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2
/usr/share/package-licenses/ripgrep/c1f96d6a54446beefad79ef49b3c123c597b7a40
/usr/share/package-licenses/ripgrep/c4f8de16c29dc84a94d610b716fb1c9c7f143582
/usr/share/package-licenses/ripgrep/c797cef3f1b13a960a5119a084fb88529a924fd7
/usr/share/package-licenses/ripgrep/ce3a2603094e799f42ce99c40941544dfcc5c4a5
/usr/share/package-licenses/ripgrep/dd445710e6e4caccc4f8a587a130eaeebe83f6f6
/usr/share/package-licenses/ripgrep/e22df6a40db2eb4307dbc53b2cffa548e2bcbd2c
/usr/share/package-licenses/ripgrep/ec9737a4e769cce48d5c95d9c75a4ba5f29a2563
/usr/share/package-licenses/ripgrep/f2515ca1c978fa1b1d6e13a8a9ae63a36a2d52cd
/usr/share/package-licenses/ripgrep/f9cc84dfc567fdc0979fddc3e6257191d8ebc9d8
/usr/share/package-licenses/ripgrep/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85
/usr/share/package-licenses/ripgrep/ff3ed70db4739b3c6747c7f624fe2bad70802987
