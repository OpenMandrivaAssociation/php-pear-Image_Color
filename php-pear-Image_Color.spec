%define _class		Image
%define _subclass	Color
%define modname	%{_class}_%{_subclass}

Summary:	Manage and handles color data and conversions
Name:		php-pear-%{modname}
Version:	1.0.4
Release:	10
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Image_Color/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	php-pear
Requires:	php-gd
Requires(post,preun):	php-pear
Requires:	php-pear

%description
Manage and handles color data and conversions.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/%{_class}/Tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

