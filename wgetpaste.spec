Name:           wgetpaste
Version:        2.30.1
Release:        1%{?dist}
Summary:        Command-line interface to various paste-bins

License:        MIT
URL:            https://github.com/nvinson/%{name}/
Source0:        ${url}/archive/refs/tags/${version}.tar.gz

Requires:       bash sed wget

BuildArch:      noarch

%description
Command-line interface to various paste-bins

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}

install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
sed -i -e "s:/usr/bin/env bash:/bin/bash:" %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE


%changelog
* Tue Oct 1 2019 Wulf C. Krueger <wk@mailstation.de> 2.29-1
- Update to 2.29

* Wed Mar 21 2018 Wulf C. Krueger <wk@mailstation.de> 2.28-1
- Initial package
