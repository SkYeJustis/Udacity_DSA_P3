# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None, description=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler, description)


    def insert(self, path_parts, description):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for h in path_parts:
            current_node.insert(h)
            current_node = current_node.children[h]
        current_node.is_handler = True
        current_node.description = description

    def find(self, path_paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for h in path_paths:
            if h in current_node.children:
                current_node = current_node.children[h]
            else:
                return None
        return current_node


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None, description=None):
        # Initialize the node with children as before, plus a handler
        # self.handler = handler
        self.children = {}
        self.is_handler = False
        self.description = description
        self.handler = handler

    def insert(self, handler):
        # Insert the node as before
        for h in handler.split('/'):
            if h not in self.children:
                self.children[h] = RouteTrieNode()


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, description):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(handler, description)


    def add_handler(self, handler, description):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if not isinstance(handler, str):
            print("Please input a str type 'handler' with / to separate pages")
            return

        path_parts = self.split_path(handler)
        self.trie.insert(path_parts, description)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        try:
            result = self.trie.find(self.split_path(path)).description
        except:
            result = None
        if path == '/':
            result = self.trie.root.handler
        return result


    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        return path.split('/')


if __name__ == '__main__':
    # Here are some test cases and expected outputs you can use to test your implementation

    ## Default test case
    # create the router and add a route
    router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route
    # some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
    print()

    ## Edge cases
    # create the router and add a route
    router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler(None, "invalid handler")  # attempt to add a route, but will obtain a print message stating that the attempt failed
    router.add_handler(12.1, "invalid handler")  # attempt to add a route, but will obtain a print message stating that the attempt failed
    router.add_handler(["hello", "world"], "invalid handler")  # attempt to add a route, but will obtain a print message stating that the attempt failed

    # some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
    print()

    ## More complex cases
    # create the router and add a route
    router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/main/contact", "contact handler")  # add a route
    router.add_handler("/main/about", "about handler")  # add a route
    router.add_handler("/main/past clients", "past clients handler")  # add a route
    router.add_handler("/main/past clients/1", "past clients: 1 handler")  # add a route
    router.add_handler("/main/past clients/1/a", "past clients: 1a handler")  # add a route
    # some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/main"))  # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/main/contact"))  # should print 'contact handler'
    print(router.lookup("/main/about"))  # should print 'about handler'
    print(router.lookup("/main/past clients"))  # should print 'past clients handler'
    print(router.lookup("/main/past clients/1"))  # should print 'past clients: 1 handler'
    print(router.lookup("/main/past clients/1/a"))  # should print 'past clients: 1a handler'
    # Handling unavailable links
    print(router.lookup("/main/contact/"))  # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/main/contact/me")) # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/main/past clients/1/a/"))  # should print 'about handler' or None if you did not handle trailing slashes
    print()