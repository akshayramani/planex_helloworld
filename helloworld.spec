Name:		helloworld
Version:	0.1
Release:	1
Summary:	Example planex spec file

Group:		Development/Other
License:	GPL
URL:		https://github.com/akshayramani/planex_helloworld
Source0:	https://github.com/akshayramani/planex_helloworld/archive/v%{version}.tar.gz


%description
Example spec file for dummy package

%prep
%setup -q -n planex_%{name}-%{version}

%build
make

%install
rm -rf %{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
helloworld



%changelog

