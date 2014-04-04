Name:		helloworld
Version:	0.1
Release:	1
Summary:	Hello world for spec file

Group:		Development/Other	
License:	BSD3
URL:		http://github.com/akshayramani/planex_helloworld
Source0:	git://github.com/akshayramani/planex_helloworld


%description
A hello world spec file

%prep
%setup -q


%install
rm -rf %{buildroot}
find . | cpio -pdmv %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)



%changelog

