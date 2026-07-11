%global tl_name step
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.5
Release:	%{tl_revision}.1
Summary:	A free Times-like font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/step
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/step.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/step.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The STEP fonts are a free Times-like (i.e., Times replacement) font
family, implementing a design first created for The Times of London in
1932. These fonts are meant to be compatible in design with Adobe's
digitization of Linotype Times, commonly used in publishing. The fonts
were forked from XITS/STIX and Type 1 support is provided for legacy TeX
engines.

