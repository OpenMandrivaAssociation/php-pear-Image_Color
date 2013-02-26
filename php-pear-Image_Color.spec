%define		_class		Image
%define		_subclass	Color
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.4
Release:	%mkrel 3
Summary:	Manage and handles color data and conversions
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Image_Color/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires:	php-gd
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Manage and handles color data and conversions.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/%{_class}/Tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2011.0
+ Revision: 667531
- mass rebuild

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 569596
- update to new version 1.0.4

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-4mdv2010.1
+ Revision: 479364
- don't ship test files

* Fri Dec 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-3mdv2010.1
+ Revision: 473542
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.3-2mdv2010.0
+ Revision: 426650
- rebuild

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 1.0.3-1mdv2009.1
+ Revision: 324521
- update to new version 1.0.3

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-4mdv2009.0
+ Revision: 224751
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-3mdv2008.1
+ Revision: 178521
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2007.0
+ Revision: 81170
- Import php-pear-Image_Color

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdk
- new group (Development/PHP)

* Wed Sep 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdk
- 1.0.2

* Thu Aug 25 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-7mdk
- rebuilt to fix auto deps

* Tue Aug 09 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sat Jul 30 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-5mdk
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-4mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdk
- fix deps

* Mon Jul 18 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdk
- fix spec file to conform with the others

* Sat May 28 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdk
- initial Mandriva package

