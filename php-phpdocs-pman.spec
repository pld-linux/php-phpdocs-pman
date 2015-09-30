%define		status		stable
%define		pearname	pman
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - PHP Unix manual pages
Name:		php-phpdocs-pman
# To check for new versions:
# $ pear remote-info doc.php.net/pman
Version:	2015.06.19
Release:	1
License:	Creative Commons Attribution 3.0
Group:		Development/Languages/PHP
Source0:	http://doc.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	70ba6741354770cc4996873f997ccd4f
URL:		http://doc.php.net/package/pman/
BuildRequires:	php-channel(doc.php.net)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	man-db
Requires:	php(zlib)
Requires:	php-channel(doc.php.net)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpdocdir	%{_docdir}/phpdoc

%description
Unix manual pages of the PHP documentations from php.net.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup -d doc_dir=%{_phpdocdir}

cat <<'EOF' >.%{_bindir}/pman
#!/bin/sh
exec %{_bindir}/man -M %{_phpdocdir}/pman "$@"
EOF

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir},%{_phpdocdir}}
cp -a ./%{php_pear_dir}/.registry $RPM_BUILD_ROOT%{php_pear_dir}

cp -a ./%{_phpdocdir}/pman  $RPM_BUILD_ROOT%{_phpdocdir}

install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/pman
%dir %{_phpdocdir}/pman
%dir %{_phpdocdir}/pman/man3
%{_phpdocdir}/pman/man3/*.3*
