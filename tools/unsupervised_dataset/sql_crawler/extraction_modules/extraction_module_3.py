from bs4 import BeautifulSoup

class ExtractionModule3:
    
    def find_queries(self):
        """ Finds queries and extracts them from websites.
        
        Args:
            html: HTML response which contains HTML text
            
        Returns
            A list of queries in the form of strings.
        """
        
        soup = BeautifulSoup(self.text, "html.parser")
        code_blocks = soup.find_all("code", class_="language-sql")
        return [block.contents[0] for block in code_blocks]