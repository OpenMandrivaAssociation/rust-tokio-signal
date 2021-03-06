# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate tokio-signal

Name:           rust-%{crate}
Version:        0.2.9
Release:        1%{?dist}
Summary:        Implementation of an asynchronous Unix signal handling backed futures

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/tokio-signal
Source:         %{crates_source}
# Initial patched metadata
# * No windows
Patch0:         tokio-signal-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Implementation of an asynchronous Unix signal handling backed futures.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Feb 06 2020 Josh Stone <jistone@redhat.com> - 0.2.9-1
- Update to 0.2.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 20:02:14 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.7-3
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Josh Stone <jistone@redhat.com> - 0.2.7-1
- Update to 0.2.7

* Thu Nov 15 2018 Josh Stone <jistone@redhat.com> - 0.2.6-1
- Update to 0.2.6

* Fri Nov 09 2018 Josh Stone <jistone@redhat.com> - 0.2.5-2
- Adapt to new packaging

* Sat Sep 08 2018 Josh Stone <jistone@redhat.com> - 0.2.5-1
- Update to 0.2.5

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Tue May 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Sat Mar 10 2018 Josh Stone <jistone@redhat.com> - 0.1.5-1
- Update to 0.1.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Sat Jan 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-1
- Initial package
