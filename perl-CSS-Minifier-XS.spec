#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	CSS
%define		pnam	Minifier-XS
Summary:	CSS::Minifier::XS - XS based CSS minifier
Name:		perl-CSS-Minifier-XS
Version:	0.13
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CSS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	310e620a4dd264a55696b5e4f8224428
URL:		http://search.cpan.org/dist/CSS-Minifier-XS/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CSS::Minifier::XS is a CSS "minifier"; its designed to remove un-necessary
whitespace and comments from CSS files, while also not breaking the CSS.

CSS::Minifier::XS is similar in function to CSS::Minifier, but is
substantially faster as its written in XS and not just pure Perl.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
        INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/CSS/Minifier
%{perl_vendorarch}/CSS/Minifier/*.pm
%dir %{perl_vendorarch}/auto/CSS/Minifier
%dir %{perl_vendorarch}/auto/CSS/Minifier/XS
%attr(755,root,root) %{perl_vendorarch}/auto/CSS/Minifier/XS/*.so
%{_mandir}/man3/*
