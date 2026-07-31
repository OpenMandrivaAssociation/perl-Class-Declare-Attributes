%define upstream_name    Class-Declare-Attributes
%define upstream_version 0.12
Name:		perl-%{upstream_name}
Version:	0.12
Release:	7

Summary:	Class-Declare-Attributes module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/denormal/perl-Class-Declare-Attributes
Source0:	https://cpan.metacpan.org/authors/id/I/IB/IBB/Class-Declare-Attributes-0.12.tar.gz

BuildRequires:	make
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
%setup -q -n Class-Declare-Attributes-0.12

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
make test || :

%check
make test || :

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class/Declare/Attributes.pm
%{_mandir}/*/*

