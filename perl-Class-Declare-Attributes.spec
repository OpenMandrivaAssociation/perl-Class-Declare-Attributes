%define real_name Class-Declare-Attributes

Summary:	Class-Declare-Attributes module for perl 
Name:		perl-%{real_name}
Version:	0.04
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/I/IB/IBB/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-Class-Declare
BuildRequires:  perl-Test-Exception
%if %{mdkversion} < 1010
Buildrequires: perl-devel
%endif
BuildArch:	noarch

%description
Class::Declare::Attributes extends Class::Declare by adding support for
Perl attributes for specifying class method types. This extension was
inspired by Damian Conway's Attribute::Handlers module, and Tatsuhiko
Miyagawa's Attribute::Protected module.

%prep
%setup -q -n %{real_name}-%{version} 

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


