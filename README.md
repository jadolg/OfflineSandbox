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