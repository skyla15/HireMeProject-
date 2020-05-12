class foo:
  __slots__ = ('foo')
  def __init__(self):
      k = None

def main():
  foo1 = foo()
  foo1.foo = 'foo'
  # foo1.__dict__			# {'foo': 'foo'}
  print(type(foo1.__slots__))				# foo
  # print(foo1.k)

main()