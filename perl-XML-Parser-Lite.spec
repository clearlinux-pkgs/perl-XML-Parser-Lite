#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-Parser-Lite
Version  : 0.722
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/P/PH/PHRED/XML-Parser-Lite-0.722.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PH/PHRED/XML-Parser-Lite-0.722.tar.gz
Summary  : 'Lightweight pure-perl XML Parser (based on regexps)'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Requires)

%description
NAME
XML::Parser::Lite - Lightweight regexp-based XML parser
SYNOPSIS
use XML::Parser::Lite;

%package dev
Summary: dev components for the perl-XML-Parser-Lite package.
Group: Development
Provides: perl-XML-Parser-Lite-devel

%description dev
dev components for the perl-XML-Parser-Lite package.


%prep
%setup -q -n XML-Parser-Lite-0.722

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/XML/Parser/Lite.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::Parser::Lite.3
