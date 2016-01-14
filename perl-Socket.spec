%{?scl:%scl_package perl-Socket}
%{!?scl:%global pkg_name %{name}}

%global cpan_version 2.013
Name:           %{?scl_prefix}perl-Socket
Epoch:          1
Version:        %(echo '%{cpan_version}' | tr '_' '.')
Release:        2%{?dist}
Summary:        Networking constants and support functions
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Socket/
Source0:        http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/Socket-%{cpan_version}.tar.gz
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::CBuilder)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Constant) >= 0.23
# ExtUtils::Constant::ProxySubs not used
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
# Scalar::Util is needed only if getaddrinfo(3) does not exist. Not our case.
BuildRequires:  %{?scl_prefix}perl(warnings::register)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
# Tests only:
BuildRequires:  %{?scl_prefix}perl(Errno)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%{?perl_default_filter}

%description
This module provides a variety of constants, structure manipulators and other
functions related to socket-based networking. The values and functions
provided are useful when used in conjunction with Perl core functions such as
socket(), setsockopt() and bind(). It also provides several other support
functions, mostly for dealing with conversions of network addresses between
human-readable and native binary forms, and for hostname resolver operations.

%prep
%setup -q -n Socket-%{cpan_version}

%build
%{?scl:scl enable %{scl} '}
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{?scl:'}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Artistic Changes Copying LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Socket*
%{_mandir}/man3/*

%changelog
* Thu Feb 13 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.013-2
- Removed useless filter of dependencies
- Resolves: rhbz#1064855

* Wed Nov 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.013-1
- 2.013 bump

* Wed Feb 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.009-1
- SCL package - initial import
