%global tl_name pst-mirror
%global tl_revision 71294

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02a
Release:	%{tl_revision}.1
Summary:	Images on a spherical mirror
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-mirror
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-mirror.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-mirror.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands and supporting PostScript material for
drawing images as if reflected by a spherical mirror.

