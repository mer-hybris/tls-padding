Name:       libtls-padding
Version:    1
Release:    1
Summary:    Reserve some TLS spaces
License:    Unknown
URL:        https://gitlab.com/ubports/core/hybris-support/tls-padding

%description
Doesn't do anything but reserve some TLS spaces.

%prep
# we have no source, so nothing here

%build
make

%install
mkdir -p %{buildroot}%{_libdir}
install -m 755 libtls-padding.so %{buildroot}%{_libdir}/libtls-padding.so

%files
%{_libdir}/libtls-padding.so
