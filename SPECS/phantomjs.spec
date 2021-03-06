Summary:	Scriptable Headless WebKit
Name:		phantomjs
Version:	2.0.0
Release:	1.vortex%{?dist}
Vendor:		Vortex RPM
License:	BSD
Group:		Utilities/Misc
URL:		http://phantomjs.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	gperf
BuildRequires:	ruby
BuildRequires:	openssl-devel
BuildRequires:	freetype-devel
BuildRequires:	fontconfig-devel
BuildRequires:	libicu-devel
BuildRequires:	sqlite-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
PhantomJS is a headless WebKit with JavaScript API. It has fast and native
support for various web standards: DOM handling, CSS selector, JSON,
Canvas, and SVG. PhantomJS is created by Ariya Hidayat.

%prep
%setup -q

%build
./build.sh --confirm

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}/examples
cp examples/* %{buildroot}%{_datadir}/%{name}/examples/
install -D -p -m 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}/examples
%doc CONTRIBUTING.md ChangeLog LICENSE.BSD README.md

%changelog
* Tue Dec 29 2015 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 2.0.0-1.vortex
- Update to 2.0.0.

* Fri Dec 25 2015 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 1.9.7-1.vortex
- Initial packaging.
