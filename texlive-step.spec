Name:		texlive-step
Version:	57307
Release:	2
Summary:	A free Times-like font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/step
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/step.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/step.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The STEP fonts are a free Times-like (i.e., Times replacement)
font family, implementing a design first created for The Times
of London in 1932. These fonts are meant to be compatible in
design with Adobe's digitization of Linotype Times, commonly
used in publishing. The fonts were forked from XITS/STIX and
Type 1 support is provided for legacy TeX engines.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/step
%{_texmfdistdir}/fonts/vf/public/step
%{_texmfdistdir}/fonts/type1/public/step
%{_texmfdistdir}/fonts/tfm/public/step
%{_texmfdistdir}/fonts/opentype/public/step
%{_texmfdistdir}/fonts/map/dvips/step
%{_texmfdistdir}/fonts/enc/dvips/step
%doc %{_texmfdistdir}/doc/fonts/step

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
