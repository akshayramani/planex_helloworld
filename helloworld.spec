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
%setup -q 

%install
rm -rf %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc



%changelog
Initial commit
Akshay Ramani <akshay.ramani@citrix.com>
