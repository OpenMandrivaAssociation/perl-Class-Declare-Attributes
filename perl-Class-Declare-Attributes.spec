%define upstream_name    Class-Declare-Attributes
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Class-Declare-Attributes module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/I/IB/IBB/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Class-Declare
BuildRequires:  perl-Test-Exception
%if %{mdkversion} < 1010
Buildrequires: perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Class::Declare::Attributes extends Class::Declare by adding support for
Perl attributes for specifying class method types. This extension was
inspired by Damian Conway's Attribute::Handlers module, and Tatsuhiko
Miyagawa's Attribute::Protected module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class/Declare/Attributes.pm
%{_mandir}/*/*
