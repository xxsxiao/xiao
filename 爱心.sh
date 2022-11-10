#!/system/bin/sh
if [ `id -u` -ne 0 ]; then
	echo "请root执行"
	exit
fi
skip=48
set -e
tab='	'
nl='
'
IFS=" $tab$nl"
umask=`umask`
umask 77
gztmpdir=
trap 'res=$?
  test -n "$gztmpdir" && rm -fr "$gztmpdir"
  (exit $res); exit $res
' 0 1 2 3 5 10 13 15
case $TMPDIR in
  / | /*/) ;;
  /*) TMPDIR=$TMPDIR/;;
  *) TMPDIR=/data/adb/;;
esac
if type mktemp >/dev/null 2>&1; then
  gztmpdir=`mktemp -d "${TMPDIR}gztmpXXXXXXXXX"`
else
  gztmpdir=${TMPDIR}gztmp$$; mkdir $gztmpdir
fi || { (exit 127); exit 127; }
gztmp=$gztmpdir/$0
case $0 in
-* | */*'
') mkdir -p "$gztmp" && rm -r "$gztmp";;
*/*) gztmp=$gztmpdir/`basename "$0"`;;
esac || { (exit 127); exit 127; }
case `printf 'X\n' | tail -n +1 2>/dev/null` in
X) tail_n=-n;;
*) tail_n=;;
esac
if tail $tail_n +$skip <"$0" | gzip -cd > "$gztmp"; then
  umask $umask
  chmod 700 "$gztmp"
  (sleep 5; rm -fr "$gztmpdir") 2>/dev/null &
  "$gztmp" ${1+"$@"}; res=$?
else
  printf >&2 '%s\n' "Cannot decompress $0"
  (exit 127); res=127
fi; exit $res
�     ���J�0�s�?Je�j4��Dk="^|�n��6��Q�&�=
��7o����A|��&ݺ�N�9��m�&Ix�d
d���c�}�]<dW���f?�Ϻ��6D�G�_8������{v�������Se&f^;�Lkh�	��H��A����� �u߄]����C'F2 ��(��XJ�Iu�7i�h)=�Ж%D��|�V�������$��J���px4&�h$�^Y�B��*�X�3J�[.��U�e��Yb�%�n�3�R����	CH��fӇQ�G�cl��56p��:R�J���u=
���4EY��06��������G�Y�{́Jɦy���ot  
