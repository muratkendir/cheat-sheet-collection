
class WFS:

  """
  :version:
  :author:
  """

  """ ATTRIBUTES

  version  (private)

  """

  def GETCAPABILITIES(self, SERVICE:  = WFS, Version: , REQUEST:  = GETCAPABILITIES, AcceptVersions: , AcceptFormats: , Sections: ):
    """
     

    @param  SERVICE : 
    @param  Version : 
    @param  REQUEST : 
    @param  AcceptVersions : 
    @param  AcceptFormats : 
    @param  Sections : 
    @return  :
    @author
    """
    pass

  def GETFEATURE(self, SERVICE:  = WFS, VERSION: , REQUEST:  = GETFEATURE, TYPENAMES: , FeatureId: , Count: , SortBy: , PropertyName: , Bbox: , SrsName: , Filter: , Filter_Language: , StartIndex: , OutputFormat: , ResultType: , Resolve: , ResolveDepth: , ResolveTimeout: ):
    """
     

    @param  SERVICE : 
    @param  VERSION : 
    @param  REQUEST : 
    @param  TYPENAMES : 
    @param  FeatureId : 
    @param  Count : 
    @param  SortBy : 
    @param  PropertyName : 
    @param  Bbox : 
    @param  SrsName : 
    @param  Filter : 
    @param  Filter_Language : 
    @param  StartIndex : 
    @param  OutputFormat : 
    @param  ResultType : 
    @param  Resolve : 
    @param  ResolveDepth : 
    @param  ResolveTimeout : 
    @return  :
    @author
    """
    pass

  def DESCRIBEFEATURETYPE(self, SERVICE:  = WFS, VERSION: , REQUEST:  = DESCRIBEFEATURETYPE, TYPENAMES: , OutputFormat: , Exceptions: ):
    """
     

    @param  SERVICE : 
    @param  VERSION : 
    @param  REQUEST : 
    @param  TYPENAMES : 
    @param  OutputFormat : 
    @param  Exceptions : 
    @return  :
    @author
    """
    pass

  def LISTSTOREDQUERIES(self, VERSION:  = 2.0.0, REQUEST:  = LISTSTOREDQUERIES):
    """
     

    @param  VERSION : 
    @param  REQUEST : 
    @return  :
    @author
    """
    pass

  def DESCRIBESTOREDQUERIES(self, VERSION:  = 2.0.0, REQUEST:  = DESCRIBESTOREDQUERIES, STOREDQUERY_ID: ):
    """
     

    @param  VERSION : 
    @param  REQUEST : 
    @param  STOREDQUERY_ID : 
    @return  :
    @author
    """
    pass

  def GetPropertyValue(self, SERVICE:  = WFS, VERSION:  = 2.0.0, REQUEST:  = GetPropertyValue, TYPENAMES: , VALUEREFERENCE: , Aliases: , ResolvePath: , Filter: , Filter_Language: , OutputFormat: , ResultType: , StartIndex: , Count: , Resolve: , ResolveDepth: , ResolveTimeout: , SrsName: , Bbox: , SortBy: ):
    """
     

    @param  SERVICE : 
    @param  VERSION : 
    @param  REQUEST : 
    @param  TYPENAMES : 
    @param  VALUEREFERENCE : 
    @param  Aliases : 
    @param  ResolvePath : 
    @param  Filter : 
    @param  Filter_Language : 
    @param  OutputFormat : 
    @param  ResultType : 
    @param  StartIndex : 
    @param  Count : 
    @param  Resolve : 
    @param  ResolveDepth : 
    @param  ResolveTimeout : 
    @param  SrsName : 
    @param  Bbox : 
    @param  SortBy : 
    @return  :
    @author
    """
    pass

  def GetFeatureWithLock(self, SERVICE:  = WFS, VERSION:  = 2.0.0, REQUEST:  = GetFeatureWithLock, TYPENAMES: , FeatureId: , Count: , SortBy: , PropertyName: , Bbox: , SrsName: , Filter: , Filter_Language: , StartIndex: , OutputFormat: , ResultType: , Expiry: , LockAction: , Resolve: , ResolveDepth: , ResolveTimeout: ):
    """
     

    @param  SERVICE : 
    @param  VERSION : 
    @param  REQUEST : 
    @param  TYPENAMES : 
    @param  FeatureId : 
    @param  Count : 
    @param  SortBy : 
    @param  PropertyName : 
    @param  Bbox : 
    @param  SrsName : 
    @param  Filter : 
    @param  Filter_Language : 
    @param  StartIndex : 
    @param  OutputFormat : 
    @param  ResultType : 
    @param  Expiry : 
    @param  LockAction : 
    @param  Resolve : 
    @param  ResolveDepth : 
    @param  ResolveTimeout : 
    @return  :
    @author
    """
    pass

  def LockFeature(self, SERVICE:  = WFS, VERSION: , REQUEST:  = LockFeature, TYPENAMES: , SrsName: , Filter: , Filter_Language: , ResourceId: , Bbox: , SortBy: , STOREDQUERY_ID: , StoredQuery_Parameter: , LockId: , Expiry: , LockAction: ):
    """
     

    @param  SERVICE : 
    @param  VERSION : 
    @param  REQUEST : 
    @param  TYPENAMES : 
    @param  SrsName : 
    @param  Filter : 
    @param  Filter_Language : 
    @param  ResourceId : 
    @param  Bbox : 
    @param  SortBy : 
    @param  STOREDQUERY_ID : 
    @param  StoredQuery_Parameter : 
    @param  LockId : 
    @param  Expiry : 
    @param  LockAction : 
    @return  :
    @author
    """
    pass

  def CreateStoredQuery(self, SERVICE:  = WFS, VERSION:  = 2.0.0, REQUEST:  = CreateStoredQuery, Language: ):
    """
     

    @param  SERVICE : 
    @param  VERSION : 
    @param  REQUEST : 
    @param  Language : 
    @return  :
    @author
    """
    pass

  def DropStoredQuery(self, SERVICE:  = WFS, VERSION:  = 2.0.0, REQUEST:  = DropStoredQuery, STOREDQUERY_ID: ):
    """
     

    @param  SERVICE : 
    @param  VERSION : 
    @param  REQUEST : 
    @param  STOREDQUERY_ID : 
    @return  :
    @author
    """
    pass

  def Transaction(self, SERVICE:  = WFS, VERSION:  = 2.0.0, Request:  = Transaction, lockId: , ReleaseAction: , SrsName: , InputFormat: , VendorId: ):
    """
     

    @param  SERVICE : 
    @param  VERSION : 
    @param  Request : 
    @param  lockId : 
    @param  ReleaseAction : 
    @param  SrsName : 
    @param  InputFormat : 
    @param  VendorId : 
    @return  :
    @author
    """
    pass



