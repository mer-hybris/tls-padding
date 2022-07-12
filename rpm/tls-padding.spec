Name:       libtls-padding
Version:    1
Release:    1
Summary:    Reserve some TLS spaces
License:    MIT
URL:        https://github.com/mer-hybris/tls-padding
Source0:    %{name}-%{version}.tar.gz

%description
Doesn't do anything but reserve some TLS spaces.

%prep
%setup -q

%build
make -C tls-padding

%install
mkdir -p %{buildroot}%{_libdir}
install -m 755 tls-padding/libtls-padding.so %{buildroot}%{_libdir}/libtls-padding.so

%files
%license tls-padding/LICENSE
%{_libdir}/libtls-padding.so
