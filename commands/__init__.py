from .start import startCommand
from .proofs import proofCollection, approvalButtonFunc, deleteFunc, cancelFunc, confirmFunc
from .say import saySomething

def registerCommands(bot):
    startCommand(bot)
    saySomething(bot)
    proofCollection(bot)
    approvalButtonFunc(bot)
    deleteFunc(bot)
    cancelFunc(bot)
    confirmFunc(bot)