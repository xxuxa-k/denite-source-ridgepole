from .base import Base
import os
import re

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'ridgepole'
        self.kind = 'file'

    def on_init(self, context):
        context['__bufnr'] = str(self.vim.call('bufnr', '%'))

    def gather_candidates(self, context):
        schemafile_path = self.vim.eval("g:denite_source_ridgepole#schemafile_path")
        if os.path.exists(schemafile_path) == False:
            return []
        candidates = []

        with open(schemafile_path, 'r') as schemafile:
            for line_num, line in enumerate(schemafile, 1):
                l = line.strip()
                if l == '' or l.startswith('#') or l.startswith('end'):
                    continue
                elif l.startswith('require'):
                        m = re.match("^require\s'(.+)'", l)
                        required_schemafile_path = os.path.join(os.path.dirname(schemafile.name), m.group(1))
                        if os.path.exists(required_schemafile_path):
                            partial_candidates = self._gather_candidates_from_required_schemafile(required_schemafile_path)
                            for candidate in partial_candidates:
                                candidates.append(candidate)
                            
                else:
                    candidates.append({
                        'word': line,
                        'action__path': schemafile_path,
                        'action__line': line_num
                        })

        return candidates


    def _gather_candidates_from_required_schemafile(self, required_schemafile_path):
        candidates = []
        with open(required_schemafile_path, 'r') as required_schemafile:
            for line_num, line in enumerate(required_schemafile, 1):
                l = line.strip()
                if l == '' or l.startswith('#') or l.startswith('end'):
                    continue
                else:
                    candidates.append({
                        'word': required_schemafile_path + ' ' + line,
                        'action__path': required_schemafile_path,
                        'action__line': line_num
                    })
        return candidates
