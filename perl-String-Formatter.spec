%define upstream_name    String-Formatter
%define upstream_version 0.102084

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Ways to put String::Formatter to use
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/String/String-Formatter-%{upstream_version}.tar.gz
Source1:	%{name}.rpmlintrc

BuildRequires:	perl-devel
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Sub::Exporter)
BuildArch:	noarch

%description
String::Formatter is a tool for building sprintf-like formatting routines.
It supports named or positional formatting, custom conversions, fixed
string interpolation, and simple width-matching out of the box. It is easy
to alter its behavior to write new kinds of format string expanders. For
most cases, it should be easy to build all sorts of formatters out of the
options built into String::Formatter.

Normally, String::Formatter will be used to import a sprintf-like routine
referred to as "'stringf'", but which can be given any name you like. This
routine acts like sprintf in that it takes a string and some inputs and
returns a new string:

  my $output = stringf "Some %a format %s for you to %u.\n", { ... };

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.102.82-2mdv2011.0
+ Revision: 656967
- rebuild for updated spec-helper

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.102.82-1mdv2011.0
+ Revision: 596650
- update to 0.102082

* Thu Jul 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.102.80-1mdv2011.0
+ Revision: 563001
- update to 0.102080

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.101.620-1mdv2011.0
+ Revision: 552634
- update to 0.101620

* Mon Mar 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.720-1mdv2010.1
+ Revision: 519957
- update to 0.100720

* Thu Mar 11 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.690-1mdv2010.1
+ Revision: 518084
- update to 0.100690

* Wed Mar 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.680-1mdv2010.1
+ Revision: 517307
- update to 0.100680

* Thu Nov 26 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.221-1mdv2010.1
+ Revision: 470288
- import perl-String-Formatter


* Thu Nov 26 2009 cpan2dist 0.093221-1mdv
- initial mdv release, generated with cpan2dist

