%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	XML_GRDDL
Summary:	%{_pearname} - A PHP library for dealing with GRDDL
Summary(pl.UTF-8):	%{_pearname} - biblioteka PHP do obsługi GRDDL
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	1
License:	BSD Style
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	62282f02e0dfac3d4862c63259695c84
Patch0:		%{name}-paths.patch
URL:		http://pear.php.net/package/XML_GRDDL/
BuildRequires:	php-pear-PEAR >= 1:1.4.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTTP_Request >= 1.4.2
Requires:	php-pear-Log
Requires:	php-pear-Net_URL
Requires:	php-pear-PEAR-core >= 1.4.0
Requires:	php-pear-Validate
Requires:	php-tidy
Requires:	php-xsl
Obsoletes:	php-pear-XML_GRDDL-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Features:
 - Different XSLT engines can be used,
 - Merging of RDF results, as per spec,
 - Pretty close to passing GRDDL test suite tests.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Cechy:
 - możliwość wykorzystania różnych silników XSLT,
 - łączenie wyników RDF,
 - duża zgodność z zestawem testów GRDDL.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/XML_GRDDL/docs
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/GRDDL.php
%{php_pear_dir}/XML/GRDDL
%{php_pear_dir}/data/XML_GRDDL
