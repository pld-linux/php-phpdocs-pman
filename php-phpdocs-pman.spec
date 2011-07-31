# TODO
# - fix rpm destroying symlinks and keep pman as symlink not shell wrapper
%define		status		stable
%define		pearname	pman
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - PHP Unix manual pages
Name:		php-phpdocs-pman
Version:	2011.06.25
Release:	1
License:	Creative Commons Attribution 3.0
Group:		Development/Languages/PHP
Source0:	http://doc.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	b6a3ef728aeb3ea88438226a935fcc45
URL:		http://doc.php.net/package/pman/
BuildRequires:	php-channel(doc.php.net)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	man
Requires:	php-channel(doc.php.net)
Requires:	php-pear
Requires:	php-zlib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Unix manual pages of the PHP documentations from php.net.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

# we install to system dir, no need for wrapper
# XXX rpm converts this symlink to file F@#@$ in some __post_ scriptlets
#ln -snf %{_bindir}/man .%{_bindir}/pman

cat <<'EOF' >.%{_bindir}/pman
#!/bin/sh
exec %{_bindir}/man "$@"
EOF

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir},%{_mandir}}
cp -a ./%{php_pear_dir}/.registry $RPM_BUILD_ROOT%{php_pear_dir}

cp -a docs/pman/*  $RPM_BUILD_ROOT%{_mandir}

install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/pman
%{_mandir}/man3/*.3*
