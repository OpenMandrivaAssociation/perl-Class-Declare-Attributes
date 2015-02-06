%define upstream_name    Class-Declare-Attributes
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Class-Declare-Attributes module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/I/IB/IBB/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(Class::Declare)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Class::Declare::Attributes extends Class::Declare by adding support for
Perl attributes for specifying class method types. This extension was
inspired by Damian Conway's Attribute::Handlers module, and Tatsuhiko
Miyagawa's Attribute::Protected module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class/Declare/Attributes.pm
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 680819
- mass rebuild

* Tue Oct 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 586762
- update to new version 0.08

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 405827
- rebuild using %%perl_convert_version

* Fri Jul 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2009.0
+ Revision: 238032
- update to new version 0.07

* Sat Jun 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.0
+ Revision: 216579
- update to new version 0.06

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2008.0
+ Revision: 47627
- update to new version 0.04


* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-2mdk
- Buildrequires

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.03-1mdk
- initial Mandriva package

