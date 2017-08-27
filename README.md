## Decorator to return a default value for a function when offline
Decorate your functions with a default value and set OfflineSandbox.SANDBOX to your Online/Offline status


```import OfflineSandbox

OfflineSandbox.SANDBOX = False


@OfflineSandbox.offline_sandbox_value('mundo')
def greet():
    return 'hola'

print(greet())

OfflineSandbox.SANDBOX = True

print(greet())```

You can also respond given the availability of a specific URL

```@OfflineSandbox.offline_sandbox_value('mundo', url='https://im-online.herokuapp.com/')
def greet_with_url():
    return 'hola'

print(greet_with_url())```