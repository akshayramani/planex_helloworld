Name:	 helloworld	
Version: 0.1	
Release: 1
Summary: An example helloworld package for planex	
Group:	 Applications/Systems	
License: GPL
Source0: https://github.com/akshayramani/planex_helloworld/archive/v%{version}.tar.gz	


%description
Simple package for planex

%prep
%setup -q -n planex_%{name}-%{version}/%{name}

%install
rm -rf %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)



%changelog
* Fri March 04 2014 Akshay Ramani <akshay.ramani@citrix.com>
- Initial package 
