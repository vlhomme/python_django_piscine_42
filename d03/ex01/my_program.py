from local_lib.path import Path

if __name__ == '__main__':
	d = Path('/tmp/golio')
	d.mkdir_p()
	f = Path('/tmp/golio/test.txt')
	f.touch()
	f.open()
	f.write_text("Salut tout le monde\nje vends des moutons")
	print(f.text())