Name:       libtls-padding
Version:    1
Release:    1
Summary:    Reserve some TLS spaces
License:    Unknown
URL:        https://gitlab.com/ubports/core/hybris-support/tls-padding
Source0:    %{name}-%{version}.tar.gz

%description
Doesn't do anything but reserve some TLS spaces.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}%{_libdir}
install -m 755 libtls-padding.so %{buildroot}%{_libdir}/libtls-padding.so

%files
%{_libdir}/libtls-padding.so
