Name:		testspec		
Version:	0.1
Release:	1%{?dist}
Summary:	Example planex spec file

Group:		Development/Other
License:	GPL
URL:		https://github.com/akshayramani/planex_helloworld
Source0:	https://github.com/akshayramani/planex_helloworld/archive/v%{version}.tar.gz


%description
Example spec file for dummy package

%prep
%setup -q


%install
rm -rf %{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
helloworld



%changelog

