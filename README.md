asteroid
========

A simple demonstration of how to use the python [libcloud](http://libcloud.readthedocs.org/en/latest/index.html) library with NCSA's nebula cloud.

Using libcloud
--------------

Clone this repo. Create and activate a [virtualenv](https://virtualenv.pypa.io/en/latest/). Install the requirements.

```bash
pip install -r requirements.txt
```

```bash
python ./asteroid/nebula.py
```

```python
⇝ ipython

In [1]: from asteroid import nebula

In [2]: driver = nebula.prompt_and_get_driver()
Username [jmatt] ⇝
Password ⇝

In [3]: driver.list_sizes()
Out[3]:
[<OpenStackNodeSize: id=1, name=m1.tiny, ram=512, disk=1, bandwidth=None, price=0.0, driver=OpenStack, vcpus=1,  ...>,
<OpenStackNodeSize: id=2, name=m1.small, ram=2048, disk=20, bandwidth=None, price=0.0, driver=OpenStack, vcpus=1,  ...>,
<OpenStackNodeSize: id=3, name=m1.medium, ram=4096, disk=40, bandwidth=None, price=0.0, driver=OpenStack, vcpus=2,  ...>,
<OpenStackNodeSize: id=4, name=m1.large, ram=8192, disk=80, bandwidth=None, price=0.0, driver=OpenStack, vcpus=4,  ...>,
<OpenStackNodeSize: id=5, name=m1.xlarge, ram=16384, disk=160, bandwidth=None, price=0.0, driver=OpenStack, vcpus=8,  ...>,
<OpenStackNodeSize: id=9608fe5f-7804-4a9f-b481-8e8b252b02c7, name=r1.medium, ram=8192, disk=40, bandwidth=None, price=0.0, driver=OpenStack, vcpus=2,  ...>,
<OpenStackNodeSize: id=f45017e0-d9f5-46ff-8705-5ad60668f64d, name=r2.medium, ram=16384, disk=40, bandwidth=None, price=0.0, driver=OpenStack, vcpus=2,  ...>]

```

See libcloud's documentation for additional details.

License
-------

See the LICENSE file.
